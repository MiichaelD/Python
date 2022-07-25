# https://github.com/ping/instagram_private_api
from instagram_private_api import Client


def get_followers(api, user_id):
  followers = []
  followers_result = api.user_followers(user_id, uuid)
  while True: 
     next_max_id = followers_result.get('next_max_id')
     users = followers_result.get('users', [])
     followers.extend(users)
     print('Followers: ', len(followers), '. Recently appended: ', len(users), '. Next_max_id: ', next_max_id)
     if next_max_id is None:  # No more followers left.
       break
     followers_result = api.user_followers(user_id, uuid, max_id=next_max_id)
  followers.sort(key=lambda x: x['username'])
  return followers

def get_following(api, user_id):
  following = []
  result = api.user_following(user_id, uuid)
  while True: 
     next_max_id = result.get('next_max_id')
     users = result.get('users', [])
     following.extend(users)
     print('Following: ', len(following), '. Recently appended: ', len(users), '. Next_max_id: ', next_max_id)
     if next_max_id is None:  # No more following left.
       break
     result = api.user_following(user_id, uuid, max_id = next_max_id)
  following.sort(key=lambda x: x['username'])
  return following

def users_in_common(users, user_container):
  result = []
  for user in users:
    if user in user_container:
      result.append(user.get('username'))
  return result

def user_in_container(users, target_user):
  '''
  Returns wether the target_user is part of the users.

  :param users: The list of users from which to check if target user exists.
  :param target_user: The target user to check if it is in given user list.
      It can be either the user's id or username.
  params
  '''
  for user in users:
    if user.get('username') == target_user or user.get('pk') == target_user:
      return True
  return False

def users_not_following_back(followers, following):
  followers_set = set()
  for f in followers:
    followers_set.add(f.get('username').encode("utf-8"))
  result = usernames_not_in_container(get_usernames(following), followers_set)
  return result

def usernames_not_in_container(usernames, usernames_container):
  result = []
  for username in usernames:
    if username not in usernames_container:
      result.append(username)
  return result

def usernames_not_following_back(follower_list, following_list):
  '''Returns usernames in following_list which are not follower_list'''
  followers_set = set()
  for f in follower_list:
    followers_set.add(f)
  result = usernames_not_in_container(following_list, followers_set)
  return result

def lista_elements_not_in_listb(lista, listb):
  setb = set()
  for element in listb:
    setb.add(element)
  result = usernames_not_in_container(lista, setb)
  return result

def get_usernames(user_list):
  usernames = []
  usernames_set = set()
  for user in user_list:
    username = user.get('username')
    if username not in usernames_set:
      usernames_set.add(username)
      usernames.append(username)
    else :
      print('skipped duplicated username: ', username)
  return usernames

def get_usernames_from_file(filename):
  with open(filename, 'r') as file:
    usernames = file.read().splitlines()
  return usernames

def save_usernames_to_file(filename, usernames):
  with open(filename, 'w+') as file:
    for username in usernames: 
      file.write(username)
      file.write('\n')

def print_users(users):
  for f in users:
    print(f.get('username'), '\t', f.get('full_name'), '\t', f.get('pk'))#, '\t', f.get('profile_pic_url'))
  print('Followers loaded: ', len(users))

# Getting followers and following users
api = Client(user_name, password)

# interest_user_id = mdp_user_id
followers_ = get_followers(api, interest_user_id)
following_ = get_following(api, interest_user_id)

# Getting usernames only
follower_users_ = get_usernames(followers_)  # Users following me
following_users_ = get_usernames(following_) # Users I follow

# Comparing sub-sets. - Read next line as: users I follow which are not following me:
users_not_following_back_ = usernames_not_following_back(follower_users_, following_users_)
followers_not_followed_back_ = usernames_not_following_back(following_users_, follower_users_)

# Comparing to last time checked.
# old_followers_ = get_usernames_from_file('followers.txt')
lost_followers_ = usernames_not_following_back(follower_users_, old_followers_)
new_followers_ =  usernames_not_following_back(old_followers_, follower_users_)
print('lost followers:', lost_followers_)
print('new followers:', new_followers_)

# old_following_ = get_usernames_from_file('following.txt')
lost_following_ = usernames_not_following_back(following_users_, old_following_)
new_following_ =  usernames_not_following_back(old_following_, following_users_)
print('lost following:', lost_following_)
print('new following:', new_following_)

# Update last followers usernames in file
# save_usernames_to_file('followers.txt', follower_users_) 
# save_usernames_to_file('following.txt', following_users_) 

# print_users(followers) 
# print(users_not_following_back)
