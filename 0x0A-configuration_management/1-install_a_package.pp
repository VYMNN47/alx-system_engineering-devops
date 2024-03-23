#!/usr/bin/pup
#Installs flask from pip3 using Puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package { 'Werkzeug':
  ensure   => '2.0.*',
  provider => 'pip3'
}
