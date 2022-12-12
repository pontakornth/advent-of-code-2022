require 'set'
result = 0
File.open("input.txt") do |file|
  content = file.read()
  lines = content.split("\n")
  lines.each do |line|
    first_half, second_half = line.chars.each_slice(line.chars.size / 2).to_a
    priority_char = first_half.to_set.intersection(second_half.to_set).to_a[0]
    if ('a'..'z').include?(priority_char)
      result += priority_char.ord - 96
    else
      result += priority_char.ord - 65 + 27
    end
  end
  puts result
end
