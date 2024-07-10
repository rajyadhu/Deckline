from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
   
      
      path('',views.Login),
      path('dashboard/', views.dashboard,name='dashboard'),
     # path('saveregistration/',views.saveregistration),

      #path('login/', views.login, ),
      path('checklogin/',views.checklogin),
      path("changepassword/",views.changepassword),
      path('reset_password/', views.reset_password),
      path('design/', views.design),
      path('product_category/', views.product_category),
      path("financialyear/",views.financialyear,name='fyear'),
      path("financialyearadd/", views.financialyearadd),
      path("financialyearedit/", views.financialyearedit),
      path("financialadd/",views.financialyearadd_tbl),
      path("savefinancialyear/",views.savefinancialyear),
      path("delrow/<id>",views.delete_row),
      path('basicinformation/',views.basicinformation),
      path('addinformation/',views.addinformation),
      path('dir_add/',views.addinformation),
      path('add_info_tbl/',views.dir_add),
      path('dir_edit/<id>',views.dir_edit),
      path('dir_del/<int:id>/', views.dir_del, name='dir_del'),
      path('save_edit_info/', views.save_dir_add),
      path('windowblind/',views.windowblind),
      path('windowadd/',views.windowadd),
      path('windowaddinfo/',views.windowaddinfo),
      path('windowblindedit/<id>',views.windowblindedit),
      path('windowblinddelete/<id>',views.windowblinddelete),
      path('windowsaveinfo/',views.windowsaveinfo),
      path('Product/',views.Products),
      path('addnewproduct/',views.addnewproduct),
      path('add_prod_tbl/',views.add_prod_tbl),
      path('dir_del_prod/<int:id>/', views.dir_del_prod, name='dir_del_prod'),
      path('edit_prod_tbl/<id>',views.edit_prod_tbl),
      path('save_edit_prod/',views.save_edit_prod),
      path('employeeform/',views.employeeform),
      path('saveemployeeform/',views.saveemployeeform),
      path('displayemployee/',views.displayemployee),
      path('table/',views.tablepage, name='table'),

      path('lead/',views.lead),
      path('leadadd/',views.leadadd),
      path('leadedit/<id>',views.leadedit),
      path('savelead/',views.savelead),
      path('delete_lead/<int:id>', views.delete_lead),
      path('leadedit/save_edited_lead/', views.save_edited_lead, name='save_edited_lead'),
      path( 'your-url_products/',views.ajax_view_for_products),
      path('addstaff/',views.addstaff),
      path('your-url/',views.ajax_view),
      path('salesform/',views.salesform_save),
      path('quotation',views.quotationreport),

      path('curtain/',views.curtain),
      path('addnewcurtain/',views.addnewcurtain),
      path('add_curtain_tbl/',views.add_curtain_tbl),
      path('dir_del_curtain/<int:id>/', views.dir_del_curtain, name='dir_del_curtain'),
      path('edit_curtain_tbl/<id>',views.edit_curtain_tbl),
      path('save_edit_curtain/',views.save_edit_curtain),

      path('sofa/',views.sofa),
      path('addnewsofa/',views.addnewsofa),
      path('add_sofa_tbl/',views.add_sofa_tbl),
      path('dir_del_sofa/<int:id>/', views.dir_del_sofa, name='dir_del_sofa'),
      path('edit_sofa_tbl/<id>',views.edit_sofa_tbl),
      path('save_edit_sofa/',views.save_edit_sofa),
      path('lead_report/',views.leadreport),
      path('mosquito/', views.mosquito, name='mosquito'),
      path('addmosquito/', views.addmosquito, name='addmosquito'),
      path('add_mosq_tbl/', views.add_mosq_tbl, name='add_mosq_tbl'),

   

      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

      
