


def initial_session(user,request):
    # permissions = user.roles.all().values('permissions__url').distinct()
    # permission_list = []
    # for item in permissions:
    #     permission_list.append(item['permissions__url'])
    # print(permission_list)
    #
    # request.session['permission_list'] = permission_list

    permissions = user.roles.all().values('permissions__url','permissions__group_id','permissions__action').distinct()
    permission_dict ={}

    for item in permissions:
        gid =item.get('permissions__group_id')

        if not gid in permission_dict:
            permission_dict[gid]={
                'urls':[item['permissions__url'],],
                'actions':[item['permissions__action'],]
            }
        else:
            permission_dict[gid]['urls'].append(item['permissions__url'])
            permission_dict[gid]['actions'].append(item['permissions__action'])
    print(permission_dict)

    request.session['permission_dict'] = permission_dict