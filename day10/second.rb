puts "hello"
special_cycles = [20, 60, 100, 140, 180, 220]
result = 0
x = 1
screen = "." * 240
File.open("input.txt") do |file|
    content = file.read()
    lines = content.split("\n")
    cycle = 1
    lines.each do |line|
      if line == "noop"
        if (x-1..x+1).include?((cycle - 1) % 40)
          screen[cycle - 1] = "#"
        end
        cycle += 1
      else
        round = line.split.last.to_i
        if (x-1..x+1).include?((cycle - 1) % 40)
          screen[cycle - 1] = "#"
        end
        cycle += 1
        if (x-1..x+1).include?((cycle - 1) % 40)
          screen[cycle - 1] = "#"
        end
        cycle += 1
        x += round
      end
    end
    puts screen.chars.each_slice(40).map(&:join)
    puts screen.size
end
