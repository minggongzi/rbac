import re
from django.shortcuts import render,HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin

class ValidPermission(MiddlewareMixin):
    def process_request(self,request):

        #当前路径
        current_path = request.path_info
        #检查是否属于白名单

        valid_url_list=["/login/","/reg/","/admin/.*"]
        for i in valid_url_list:
            ret=re.match(i,current_path)
            if ret:
                return None



        #校验是否登陆：

        user_id =request.session.get('user_id')
        if not user_id:
            return redirect('/login/')

        #权限列表
        # permission_list = request.session.get('permission_list',[])
        #
        # flag = False
        #
        # for permission in permission_list:
        #     permission = '^%s$' % permission
        #
        #     ret = re.match(permission, current_path)
        #     if ret:
        #         flag = True
        #         break
        # if not flag:
        #     return  HttpResponse('无访问权限')
        # return None
        permission_dict = request.session.get('permission_dict')

        for item in permission_dict.values():
            urls=item['urls']
            for reg in urls:
                reg = "^%s$" % reg
                ret = re.match(reg,current_path)
                if ret:
                    request.actions=item['actions']
                    return None
        return HttpResponse("没有访问呢权限")