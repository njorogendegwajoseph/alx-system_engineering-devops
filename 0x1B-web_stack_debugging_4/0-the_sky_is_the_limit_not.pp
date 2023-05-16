#This file increases the amount of traffic an Nginx server can handle

exec { 'fix--for-nginx':
    command => 'sed -i "s/15/4096" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

#restart Nginx now

-> exec { 'nginx-restart':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
