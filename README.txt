ansible-role-nginx
******************

Role to setup Nginx.


Variables
=========

nginx_packages_release

   Packages default release

nginx_packages
   Package with Nginx

nginx_state
   Service state

nginx_service
   Nginx service name

nginx_enable
   Enable Nginx service

nginx_config_template
   Template for Nginx main configuration file

nginx_config_file
   Main configuration file

nginx_reload
   Reload Nginx when necessary

nginx_restart
   Restart Nginx when necessary


Examples
========

   ---
   - hosts: all
     tasks:
       - import_role:
           name: nginx


Updating README
===============

   $ sphinx-build -b text . docs && cp docs/docs.txt README.txt
