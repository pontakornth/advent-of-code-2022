file = File.open('input.txt')
lines = file.read.split("\n")
result = 0
lost = ['A Z', 'B X', 'C Y']
win = ['A Y', 'B Z', 'C X']
shape_point = { 'X': 1, 'Y': 2, 'Z': 3 }
lines.each do |line|
  if lost.include?(line)
    nil
  elsif win.include?(line)
    result += 6
  else
    result += 3
  end
  # @type [String]
  shape = line[-1]
  result += shape_point[shape.to_sym]
end
puts result

file.close
