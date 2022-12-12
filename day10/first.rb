puts "hello"
special_cycles = [20, 60, 100, 140, 180, 220]
result = 0
x = 1
File.open("input.txt") do |file|
    content = file.read()
    lines = content.split("\n")
    cycle = 1
    lines.each do |line|
      p line
      puts cycle
      if line == "noop"
        cycle += 1
        if special_cycles.include?(cycle)
          puts "Cycle #{cycle} found: strength = #{cycle} * #{x} = #{cycle * x}"
          result += (cycle * x)
        end
      else
        round = line.split.last.to_i
        cycle += 1
        if special_cycles.include?(cycle)
          puts "Cycle #{cycle} found: strength = #{cycle} * #{x} = #{cycle * x}"
          result += (cycle * x)
        end
        cycle += 1
        x += round
        if special_cycles.include?(cycle)
          puts "Cycle #{cycle} found: strength = #{cycle} * #{x} = #{cycle * x}"
          result += (cycle * x)
        end
      end
    end
    puts result
end
