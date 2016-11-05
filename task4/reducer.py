#!/usr/bin/python

import sys
i = 0
post_ids = []
pre_user_id = -1
output_post_ids = []
output_user_id = -1 
for line in sys.stdin:
    line = line.strip()
    owner_user_id, post_id = line.split()
    owner_user_id = int(owner_user_id) 
    #in case of combining the anwsers of the same user
    if pre_user_id == owner_user_id:
        post_ids.append(post_id)
    #in case of combing the answers for a new user
    else:
        if pre_user_id != -1:
            #If the previous user has more anwsers, it becomes the output
            if len(post_ids) > len(output_post_ids):
                output_post_ids = list(post_ids)
                output_user_id = pre_user_id 
        #Replace previous user and update ids polls
        pre_user_id = owner_user_id
        post_ids = []
        post_ids.append(post_id)
if pre_user_id == owner_user_id:#In case of ending with a same user and his/her anwsers
    if len(post_ids) > len(output_post_ids):
        output_post_ids = list(post_ids)
        output_user_id = owner_user_id

print "OwnerUserId -> Number of accepted answers, {0} ...".format("AnswerId, "*len(output_post_ids))
print "{0} -> {1}, {2}".format(output_user_id, len(output_post_ids),', '.join(output_post_ids))
