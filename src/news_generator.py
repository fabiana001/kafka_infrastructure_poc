#from avrogen import write_schema_files
import sys, getopt

def get_args(argv):
   input_schema = None
   output_dir = None
   try:
      #opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      opts, args = getopt.getopt(argv,"ha:o:",["avro_schema=","out_dir="])
   except getopt.GetoptError:
      print('INVALID INPUT ARGS:')
      print('RUN: news_generator.py -a <avro_schema_file> -o <output_directory>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('news_generator.py -a <avro_schema_file> -o <output_directory>')
         sys.exit()
      elif opt in ("-a", "--avro_schema"):
         input_schema = arg
      elif opt in ("-o", "--out_dir"):
         output_dir = arg
   if(input_schema and output_dir):
      return input_schema, output_dir
   else:
      print('INVALID INPUT ARGS:')
      print('RUN: news_generator.py -a <avro_schema_file> -o <output_directory>')
      sys.exit(2)

def run(argv):
    from avrogen import write_schema_files
    schema_file, out_dir = get_args(argv)

    with open(schema_file, 'r') as myfile:
        schema_json = myfile.read()
    try:
        write_schema_files(schema_json, out_dir)
        print("Files correctly generated in {}".format(out_dir))

    except e:
        print(e)

if __name__ == "__main__":
   run(sys.argv[1:])
