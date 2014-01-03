#!/usr/bin/env ruby

private_key = ''
100.times do |i|
  line = "KEY_#{sprintf("%02d", i)}"
  break if ENV[line].nil?
  private_key += ENV[line] + "\n"
end
File.open(ENV['PRIVATE_KEY_FILE'], "w") { |f|
  f.puts(private_key)
}
File.chmod(0600, ENV['PRIVATE_KEY_FILE'])
