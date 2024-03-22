# create a process named killmenow 

exec { 'kill -9  killmenow' :
    path    => '/bin/',
    command => 'kill -9 killmenow',
    }
