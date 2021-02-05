require 'asciidoctor'
require 'fileutils'
require 'pathname'


def compile_asciidoc(source, destination)
  puts "#{source} -> #{destination}"

  destination.dirname.mkpath

  attributes = {
    'nofooter' => true,
    'source-highlighter' => 'pygments',
    'toc' => 'left',
  }

  Asciidoctor.convert_file(source.to_s, safe: :safe, backend: 'html', to_file: destination.to_s, attributes: attributes)
end

def guide_dist_path(path)
  source_root = Pathname.new('guides').expand_path
  target_root = Pathname.new('dist/guides').expand_path
  target_root.join(path.relative_path_from(source_root)).expand_path
end



slide_ids = Dir.chdir 'slides' do
  Dir['**/main.tex'].map do |tex_file|
    id = Pathname.new(tex_file).dirname.to_s
  end
end

namespace :slides do
  slide_ids.each do |id|
      desc "Compiles #{id}"
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

  desc 'Compiles all slides'
  task :all => [ *slide_ids ]
end

Rake::FileList.new('guides/*.asciidoc').map do |path|
  absolute_source_path = Pathname.new(path).expand_path
  absolute_target_path = guide_dist_path(absolute_source_path).sub_ext('.html')

  file absolute_target_path.to_s => absolute_source_path.to_s do |task|
    compile_asciidoc(absolute_source_path, absolute_target_path)
  end

  absolute_target_path
end.then do |paths|
  desc 'Compiles guides'
  task :guides => paths.map(&:to_s)
end

desc 'Removes dist and its contents'
task :clean do
  FileUtils.rm_r 'dist'
end

desc 'Generates everything'
task :all => [ :guides, 'slides:all' ]

desc 'Uploads everything in the dist subdirectory'
task :upload do
  `ssh -p 22345 -l upload leone.ucll.be rm -rf /home/frederic/courses/scripting/volume/docs`
  puts `scp -P 22345 -r dist upload@leone.ucll.be:/home/frederic/courses/scripting/volume/docs`
end