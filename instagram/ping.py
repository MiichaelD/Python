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


api = Client(user_name, password)
followers = get_followers(api, mdp_user_id)

for f in followers:
  print f.get('username'), '\t', f.get('full_name')#, '\t', f.get('pk'), '\t', f.get('profile_pic_url')
print 'Followers loaded: ', len(followers)