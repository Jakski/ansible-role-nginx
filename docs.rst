ansible-role-nginx
================================================================================

Role to setup Nginx.

Default configuration templates are hardcoded to make Nginx just work out of the
box. You will have to provide your own, if you plan to use this role.

Variables
--------------------------------------------------------------------------------

nginx_package_release

   Package default release

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make man

View::

   $ man ./docs/man/ansible-role-nginx.1
