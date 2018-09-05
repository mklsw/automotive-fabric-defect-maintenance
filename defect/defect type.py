#  -*- coding:UTF-8 -*-
'''
defect code  maintenance manual.
1 defect code can modified with end user.

2 defect code include supplier code ,inside code and customer code.

'''

supplier_defect_code = {'s-1':'纱结'}

inside_defect_code = {'i-1':'纱结'}

customer_defect_code ={'c-1':'厚度超标'}

defect_code = dict(supplier_defect_code,**inside_defect_code,**customer_defect_code)

print(defect_code)

