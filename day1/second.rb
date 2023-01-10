# frozen_string_literal: true

File.open('input.txt') do |file|
  # @type [String]
  content = file.read
  lines = content.split("\n")
  current = 0
  result = []
  lines.each do |line|
    if line.match(/^(\d)+$/)
      n_line = Integer(line)
      current += n_line
    else
      result.append(current)
      current = 0
    end
  end
  puts (result.sort_by { |x| -x }).take(3).reduce(&:+)
end
