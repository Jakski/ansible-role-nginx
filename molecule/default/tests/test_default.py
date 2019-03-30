import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    nginx = host.service('nginx')
    assert nginx.is_running
    assert nginx.is_enabled
    assert host.socket('tcp://0.0.0.0:80').is_listening


def test_configuration(host):
    assert not host.file('/etc/nginx/sites-enabled/default').exists
    assert host.file('/etc/nginx/nginx.conf').contains(
        r'^include /etc/nginx/modules-enabled/\*\.conf;$')
    assert host.file('/etc/nginx/nginx.conf').contains(
        r'server_names_hash_bucket_size 128;$')
    assert host.file('/etc/nginx/sites-enabled/example1.conf').contains(
        r'root /var/www/html;$')
    assert host.file('/etc/nginx/sites-enabled/example1.conf').contains(
        r'server_name www.test.local;$')
    assert host.file('/etc/nginx/sites-enabled/example2.conf').contains(
        r'root /var/www/html;$')
    assert host.file('/etc/nginx/sites-enabled/example2.conf').contains(
        r'server_name _;$')
    assert not host.file('/etc/nginx/modules-enabled/50-mod-mail.conf').exists
    assert host.file('/etc/nginx/modules-enabled/50-mod-test.conf').exists
    assert host.file('/etc/nginx/conf.d/maps.conf').contains(
        r'http_user_agent')
    assert host.file('/etc/nginx/snippets/logs.conf').contains(
        r'access_log')
