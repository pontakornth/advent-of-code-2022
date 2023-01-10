file = File.open('input.txt')
content = file.read
lines = content.split("\n")
current = 0
max_cal = 0
lines.each do |line|
  if line.match(/^(\d)+$/)
    n_line = Integer(line)
    current += n_line
  else
    max_cal = current if current > max_cal
    current = 0
  end
end
puts max_cal
