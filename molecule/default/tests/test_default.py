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
    main = host.file('/etc/nginx/nginx.conf')
    assert main.contains(
        r'^include /etc/nginx/modules-enabled/\*\.conf;$')
    assert main.contains(r'server_names_hash_bucket_size 128;$')
    example1 = host.file('/etc/nginx/sites-enabled/example1.conf')
    assert example1.contains(r'access_log /var/log/nginx/example1-access.log;$')
    assert example1.contains(r'server_name www.test.local;$')
    example2 = host.file('/etc/nginx/sites-enabled/example2.conf')
    assert example2.contains(r'access_log /var/log/nginx/example2-access.log;$')
    assert example2.contains(r'server_name _;$')
    assert not host.file('/etc/nginx/modules-enabled/50-mod-mail.conf').exists
    assert host.file('/etc/nginx/modules-enabled/50-mod-test.conf').exists
    assert host.file('/etc/nginx/conf.d/maps.conf').contains(
        r'http_user_agent')
    assert host.file('/etc/nginx/snippets/logs.conf').contains(
        r'access_log')
