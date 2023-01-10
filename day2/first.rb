file = File.open('input.txt')
lines = file.read.split("\n")
result = 0
lost = ['A Z', 'B X', 'C Y']
win = ['A Y', 'B Z', 'C X']
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
  result += case shape
            when 'X'
              1
            when 'Y'
              2
            else
              3
            end
end
puts result

file.close
