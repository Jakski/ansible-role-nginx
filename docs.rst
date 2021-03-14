ansible-role-nginx
================================================================================

Role to setup Nginx.

Variables
--------------------------------------------------------------------------------

nginx_packages_release

   Packages default release

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/converge.yml
   :language: yaml

Updating README
--------------------------------------------------------------------------------

::

   $ sphinx-build -b text . docs && cp docs/docs.txt README.txt

