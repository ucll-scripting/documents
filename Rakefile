require 'pathname'


Dir['**/main.tex'].map do |tex_file|
    id = Pathname.new(tex_file).dirname.to_s

    task id do
        puts "Compiling #{id}"
        Dir.chdir id do
            puts `pdflatex main.tex`
            puts `pdflatex main.tex`
        end
    end
end
