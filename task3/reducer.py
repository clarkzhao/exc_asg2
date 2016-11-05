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
    if pre_user_id == owner_user_id:
        post_ids.append(post_id)
    else:
        if pre_user_id != -1:
            if len(post_ids) > len(output_post_ids):
                output_post_ids = list(post_ids)
                output_user_id = pre_user_id 
        pre_user_id = owner_user_id
        post_ids = []
        post_ids.append(post_id)
if pre_user_id == owner_user_id:
    if len(post_ids) > len(output_post_ids):
        output_post_ids = list(post_ids)
        output_user_id = owner_user_id

print "OwnerUserId -> {0} ...".format("PostId, "*len(output_post_ids))
print "{0} -> {1}".format(output_user_id,', '.join(output_post_ids))
