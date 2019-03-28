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
    assert host.file('/etc/nginx/sites-enabled/example.conf').contains(
        r'root /var/www/html;$')
    assert not host.file('/etc/nginx/modules-enabled/50-mod-mail.conf').exists
    assert host.file('/etc/nginx/modules-enabled/50-mod-test.conf').exists
    assert host.file('/etc/nginx/conf.d/maps.conf').contains(
        r'http_user_agent')
    assert host.file('/etc/nginx/snippets/logs.conf').contains(
        r'access_log')
