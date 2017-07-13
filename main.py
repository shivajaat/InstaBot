import requests
import urllib
from termcolor import colored
APP_ACCESS_TOKEN = '4076541369.19c16c7.1cfc751035ea4e8e845fb7f7c72da78f'
BASE_URL = 'https://api.instagram.com/v1/'
def My_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET requests_url: %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if user_info['data']:
            print 'UserName is:%s' % (user_info['data']['username'])
            print 'Number of Followers: %s' %(user_info['data']['counts']['followed_by'])
            print 'Number of persons you are following: %s' % (user_info['data']['counts']['follows'])
            print 'Total Posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User not Exist!.....'
    else:
        print 'Staus code is other then 200 are received!.....'
def get_user_id(instagram_username):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (instagram_username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          return user_info['data'][0]['id']
      else:
          return None
  else:
      print 'Status code other than 200 received!'
def user_info(instagram_username):
    _id=get_user_id(instagram_username)
    if _id ==None:
        print 'user does not exist'
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'No data available for this user!'
    else:
            print 'Status code other than 200 received!......'
            return None
def own_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print "Your image is now downloading...."
        else:
            print 'Post not exist'
    else:
        print"status is other code"
def user_post(instagram_username):
    user_id=get_user_id(instagram_username)
    if user_id == None:
        print 'Loading.....'
        print'User not exist...'
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            image_name = user_media['data'][0]['id'] + '.jpeg'
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'
        else:
            print 'Post does not exist!'
    else:
        print 'Status code other than 200 received!'
def get_post_id(instagram_username):
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()
def like_a_post(instagram_username):
    media_id = get_post_id(instagram_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": APP_ACCESS_TOKEN}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()
    if post_a_like["meta"]["code"] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'
def list_comments(instagram_username):
    _id = get_post_id(instagram_username)
    if instagram_username == None:
        print 'User does not exit!.....'
        exit()
    else:
        request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (_id,APP_ACCESS_TOKEN)
        print 'Get request url:%s' % (request_url)
        user_media = requests.get(request_url).json()
        print user_media
        if user_media['meta']['code'] == 200:
            if len(user_media['data']):
                print 'Comments Are :--'
                position = 1
                for msg in user_media['data']:
                    print colored(' from: %s' % (msg),'yellow')
                    position = position+1
            else:
                print "No comments found"
                return None
def comment_post(instagram_username):
    media_id = get_post_id(instagram_username)
    comment_text = raw_input("Write your comment Here..: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
    comment = requests.post(request_url, payload).json()
    if comment['meta']['code'] == 200:
        print "Successfully added comment!....."
    else:
        print "Unable to add comment......"
#def get_location(lat,lng):
  # request_url = (BASE_URL + 'locations/search?lat=%s&lng=%s&access_token=%s') % (lat,lng,APP_ACCESS_TOKEN)
   #print 'get url: %s' % (request_url)


def start_bot():
    while True:
        print colored('Hey! Welcome to InstaBot!','cyan')
        print colored('Yours Menu options:-','cyan')
        print colored("a.your own details.....",'magenta')
        print colored("b.Get Id of a user by username.....",'magenta')
        print colored("c.Your own user details.....",'magenta')
        print colored("d.To view own Recent post.....",'magenta')
        print colored("e.To view user Recent post.....",'magenta')
        print colored("f.To get recent post id.....",'magenta')
        print colored("g.Like recent post of user.....",'magenta')
        print colored("h.To get list of comments on recent post of user.....",'magenta')
        print colored("i.To comment on the recent post of a user.....",'magenta')
        print colored("j.Exit.....",'magenta')
        choice = raw_input("Enter you choice: ")
        if choice == "a":
            My_info()
        elif choice == "b":
            instagram_username = raw_input("Enter the username of the user: ")
            get_user_id(instagram_username)
        elif choice == "c":
            instagram_username = raw_input("Enter user name to View details")
            user_info(instagram_username)
        elif choice == "d":
            own_post()
        elif choice == 'e':
            instagram_username = raw_input("Enter username to View post of user..... ")
            user_post(instagram_username)
        elif choice == 'f':
             instagram_username = raw_input('Enter username to view post id')
             get_post_id(instagram_username)
        elif choice == 'g':
            instagram_username = raw_input('Enter username to like post.....')
            like_a_post(instagram_username)
        elif choice == 'h':
            instagram_username = raw_input("Enter username to add a comment.....")
            list_comments(instagram_username)
        elif choice == 'i':
            instagram_username = raw_input("Enter username to add a comment.....")
            comment_post(instagram_username)
        elif choice == "j":
            exit()
        else:
            print "wrong choice"
start_bot()