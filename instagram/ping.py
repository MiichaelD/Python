from instagram_private_api import Client, ClientCompatPatch

user_name = 'michaelduartest'
user_id = 12262693300
uuid = '' # api.generate_uuid()

def get_followers(api, user_id):
  followers = []
  followers_result = api.user_followers(user_id, uuid)
  while True: 
     next_max_id = followers_result.get('next_max_id')
     users = followers_result.get('users', [])
     followers.extend(users)
     if next_max_id is None:  # No more followers left.
       break
     followers_result = api.user_followers(user_id, uuid, max_id = next_max_id)
  followers.sort(key=lambda x: x['username'])
  return followers


def get_following(api, user_id):
  following = []
  result = api.user_following(user_id, uuid)
  while True: 
     next_max_id = result.get('next_max_id')
     users = result.get('users', [])
     following.extend(users)
     if next_max_id is None:  # No more following left.
       break
     result = api.user_followers(user_id, uuid, max_id = next_max_id)
  following.sort(key=lambda x: x['username'])
  return following

def is_user_following_target(api, user_id, target_user):
  '''
  Returns wether the user is following the target_user.

  :param api: signed in client.
  :param user_id: The user's id from which to check following list.
  :param target_user: The target user to check if it is in following list.
      It can be either the user's id or username.
  params
  '''
  following = get_following(api, user_id)
  for user in following:
    if user.get('username') == target_user or user.get('pk') == target_user:
      return True
  return False


api = Client(user_name, password)
followers = get_followers(api, mdp_user_id)

for f in followers:
  print f.get('username'), '\t', f.get('full_name')#, '\t', f.get('pk'), '\t', f.get('profile_pic_url')
print 'Followers loaded: ', len(followers)
