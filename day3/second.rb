require 'set'
result = 0
File.open("input.txt") do |file|
  content = file.read()
  lines = content.split("\n")
  lines.each_slice(3) do |group|
    priority_char = group.map(&:chars).map(&:to_set).reduce(&:intersection).first
    if ('a'..'z').include?(priority_char)
      result += priority_char.ord - 96
    else
      result += priority_char.ord - 65 + 27
    end
  end
  puts result
end
