require 'fileutils'
require 'pathname'


slide_ids = Dir.chdir 'slides' do
  Dir['**/main.tex'].map do |tex_file|
    id = Pathname.new(tex_file).dirname.to_s
  end
end

namespace :slides do
  slide_ids.each do |id|
      task id do
          puts "Compiling #{id}"
          Dir.chdir "slides/#{id}" do
              puts `pdflatex main.tex`
              puts `pdflatex main.tex`
          end

          source = "slides/#{id}/main.pdf"
          target_dir = "dist/slides"
          target_file = "#{target_dir}/#{id}.pdf"
          puts "Copying #{source} to #{target_file}"

          FileUtils.mkdir_p target_dir
          FileUtils.cp source, target_file
      end
  end

  task :clean do
    FileUtils.rm_r 'dist'
  end

  task :all => [ :clean, *slide_ids ]
end




task :upload do
  Dir.chdir 'dist' do
    `ssh -p 22345 -l upload leone.ucll.be rm -rf /home/frederic/courses/scripting/volume/slides`
    puts `scp -P 22345 -r * upload@leone.ucll.be:/home/frederic/courses/scripting/volume/slides`
  end
end