#Manuscript willl enable holberton to log  in and work on files with zero errors. 

exec { 'increase-hard-file-limit-for-holb-user':
    command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}


#Increase soft file limit for user holberton

exec { 'increase-soft-file-limit-for-holberton-user':
    command => 'sed -i "/holberton soft/s/4/50000" /etc/security/limits.conf',
    path    => '/usr/local/bin/'
