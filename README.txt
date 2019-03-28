ansible-role-nginx
******************

Role to setup Nginx.

Default configuration templates are hardcoded to make Nginx just work
out of the box. You will have to provide your own, if you plan to use
this role.


Variables
=========

nginx_package_release

   Package default release

nginx_package

   Package with Nginx

nginx_service

   Nginx service name

nginx_enable

   Enable Nginx service

nginx_config_template

   Template for Nginx main configuration file

nginx_config_dir

   Directory with configuration

nginx_manage_config_fragments

   Remove unmanaged configuration fragments from conf.d

nginx_config_fragments

   Filename/content dictionary with configuration fragments for conf.d

   Extenstion .conf will be added automatically

nginx_snippets

   Filename/content dictionary with configuration snippets

   Extenstion .conf will be added automatically

nginx_vhosts

   Filename/settings dictionary with virtual hosts

   Extenstion .conf will be added automatically

nginx_vhost_template

   Template for virtual hosts

nginx_reload

   Reload Nginx when necessary

nginx_restart

   Restart Nginx when necessary

nginx_modules

   Dictionary with extra modules configuration, e.g.:

      50-mod-stream:
        enabled: false
      50-mod-mail:
        dest: /usr/share/nginx/modules-available/mod-mail.conf

nginx_manage_vhosts

   Remove unmanaged virtual hosts


Examples
========

   ---
   - hosts: instance
     tasks:
       - import_role:
           name: nginx
         vars:
           nginx_modules:
             50-mod-mail:
               enabled: false
             50-mod-test:
               content: ""
           nginx_vhosts:
             example:
           nginx_config_fragments:
             maps: |
               map $http_user_agent $mobile {
                 default       0;
                 "~Opera Mini" 1;
               }
           nginx_snippets:
             logs: |
               access_log /var/log/nginx/all.log;


Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make man

View:

   $ man ./docs/man/ansible-role-nginx.1
