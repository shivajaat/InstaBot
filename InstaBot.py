#Here we stating the InstaBot project
#Here we using libraries.....
import requests
import urllib
#Here we using termcolor from colored to view coloring.....
from termcolor import colored
#You can use SANDBOX USER these users: idilshadali , shivabalre , __nabin_

#Here we are using access tocken to access data of instagram by tocken
APP_ACCESS_TOKEN = '4076541369.19c16c7.1cfc751035ea4e8e845fb7f7c72da78f'
#Here  we using base url
BASE_URL = 'https://api.instagram.com/v1/'
calamities = ['flood','earthquake','tsunami','landslide','soil erosion', 'avalanche', 'cyclones', 'thunderstorm', 'drought']
locid = []
#Staring view of project
print colored('Hey! Welcome to InstaBot!', 'cyan')
print colored('You can use these users :idilshadali  shivabalre  __nabin_', 'cyan')
#Here my_info function are use to view information of own
def My_info():
    #here we using req url which is combination of base url or access tocken
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET requests_url: %s' % (request_url)
    user_info = requests.get(request_url).json()
    #when 200 code is occure which is use to working if everything is okk
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
#get user id function use to get user info
def get_user_id(instagram_username):
# here we using req url which is combination of base url or access tocken
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (instagram_username, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()
  # when 200 code is occure which is use to working if everything is okk

  if user_info['meta']['code'] == 200:
        if len(user_info['data']):
              #You can get id by click on just on link.....
              return user_info['data'][0]['id']

        else:
              return None
  else:
        print 'Status code other than 200 received!'
def user_info(instagram_username):
    _id=get_user_id(instagram_username)
    if _id ==None:
        print 'user does not exist'
        exit()
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
    # here we using req url which is combination of base url or access tocken
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
def calamities_post(instagram_username):
    _id = get_user_id(instagram_username)
    if _id == None:
        print 'Loading.....'
        print 'User not exist......'
    else:
        request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (_id, APP_ACCESS_TOKEN)
        print 'GET request url : %s' % (request_url)
        _media = requests.get(request_url).json()
        if _media['meta']['code'] == 200:
            if len(_media['data']):
                i=0
                v = len(_media['data'])
                for i in range(v):
                    for temp in calamities:
                        if temp in _media['data'][i]['tags']:
                            if _media['data'][i]['location'] != None:
                                id_ = _media['data'][i]['location']['id']
                                locid.append(id_)
            else:
                print 'Loading.....'
                print 'Post not exist.....'
                exit()
        else:
            print 'Loading.....'
            print 'Status code other then 200.....'
#To get post id function is used below.....
def get_post_id(instagram_username):
    # to access id.....
    user_id = get_user_id(instagram_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    # here we using req url which is combination of base url or access tocken
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
#To like a post a like_a_post function is used.....
def like_a_post(instagram_username):
    #to get post id
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
    #To get post id
    _id = get_post_id(instagram_username)
    if instagram_username == None:
        print 'User does not exit!.....'
        exit()
    else:
        # here we using req url which is combination of base url or access token
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
    #to get post id
    media_id = get_post_id(instagram_username)
    comment_text = raw_input("Write your comment Here..: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    # here we using req url which is combination of base url or access token
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
    comment = requests.post(request_url, payload).json()
    #comment will be added when 200 code occur
    if comment['meta']['code'] == 200:
        print "Successfully added comment!....."
    elif comment['meta']['code'] != 200:
        print 'Loading.....'
        print 'status is other then 200.....'
    else:
        print 'Loading.....'
        print "Unable to add comment......"
def get_location():
    for temp_id in locid:
      next_url = (BASE_URL + 'locations/%s/media/recent?access_token=%s') % (temp_id, APP_ACCESS_TOKEN)
      print 'url is ',next_url
      loc_media=requests.get(next_url).json()
      if loc_media['meta']['code']==200:
        if len(loc_media['data']):
            print 'Location is..:%s' % (loc_media['data'][0]['location']['name'])
            print loc_media['data'][0]['images']['standard_resolution']['url']
        else:
            print 'No media'
      else:
         print 'Status code other than 200 received'

#Here start bot is use to show menu
def start_bot():
    print locid
    while True:
        #All menu
        print colored('Yours Menu options:-', 'cyan')
        print colored('Please select any option.....','yellow')
        print colored("1.your own details.....",'magenta')
        print colored("2.Get Id of a user by username.....",'magenta')
        print colored("3.Your own user details.....",'magenta')
        print colored("4.To view own Recent post.....",'magenta')
        print colored("5.To view user Recent post.....",'magenta')
        print colored("6.To get recent post id.....",'magenta')
        print colored("7.Like recent post of user.....",'magenta')
        print colored("8.To get lists of comments on recent post of the user.....",'magenta')
        print colored("9.To comment on the recent post of a user.....",'magenta')
        print colored('10.GET info about natural Calamities.....','magenta')
        print colored("11.Exit.....",'magenta')
        choice = raw_input("Enter you choice: ")
        if choice == "1":
            print 'Loading.....'
            My_info()
        elif choice == "2":
            print 'Loading.....'
            instagram_username = raw_input("Enter the username of the user: ")
            get_user_id(instagram_username)
        elif choice == "3":
            print 'Loading.....'
            instagram_username = raw_input("Enter user name to View details")
            user_info(instagram_username)
        elif choice == "4":
            print 'Loading.....'
            own_post()
        elif choice == '5':
            print 'Loading.....'
            instagram_username = raw_input("Enter username to View post of user..... ")
            user_post(instagram_username)
        elif choice == '6':
             print 'Loading.....'
             instagram_username = raw_input('Enter username to view post id')
             get_post_id(instagram_username)
        elif choice == '7':
            print 'Loading.....'
            instagram_username = raw_input('Enter username to like recent post.....')
            like_a_post(instagram_username)
        elif choice == '8':
            print 'Loading.....'
            instagram_username = raw_input("Enter username to view list of comment.....")
            list_comments(instagram_username)
        elif choice == '9':
            print 'Loading.....'
            print colored('You can use these users    idilshadali ,  __nabin_  ,  shivabalre','cyan')
            instagram_username = raw_input("Enter username to add a comment.....")
            comment_post(instagram_username)
        elif choice == '10':
            print 'Loading.....'
            print 'use shivabalre user to get info'
            insta_username = raw_input("USERNAME:")
            calamities_post(insta_username)
            get_location()
        elif choice == "11":
            print 'Loading.....'
            print 'You are Done.....'
            exit()
        else:
            #it occure if something wrong occure on input.....
            print 'Loading.....(Something wrong input)'
            print "wrong choice"
Menu = raw_input(("Do you want to view menu (Y/N)? or (y/n)?......."))
if  Menu== "Y" or Menu == "y":
    print colored('Loading Menu.....','yellow')
    start_bot()
else:
    print 'Done'
    exit()

#Project Finished.....
