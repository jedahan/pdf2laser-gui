# pip3 install --user Gooey
from gooey import Gooey, GooeyParser


@Gooey(target="pdf2laser", program_name='pdf2laser', suppress_gooey_flag=True)
def main():
    parser = GooeyParser(description="send a pdf to the epilog")

    general = parser.add_argument_group('General')
    raster = parser.add_argument_group('Raster')
    vector = parser.add_argument_group('Vector')

    general.add_argument('-a',
                           metavar='Autofocus',
                           help='Enable auto focus',
                           widget='BlockCheckbox')
    general.add_argument('-n',
                           metavar='Job Name',
                           help='Set the job name to display')
    general.add_argument('-p',
                           metavar='Address',
                           default='192.168.1.4',
                           help='ip address of the printer')
    general.add_argument('-P',
                           metavar='Preset',
                           help='Select a default preset')

    raster.add_argument('-d',
                           metavar='DPI',
                           help='Resolution of raster artwork')
    raster.add_argument('-m',
                           metavar='Mode',
                           help='Mode for rasterization (default mono)')
    raster.add_argument('-r',
                           metavar='Speed',
                           gooey_options={
                                      'validator': {
                                          'test': '1 <= int(user_input) <= 100',
                                          'message': 'Must be between 1 and 100'
                                      }
                           },
                           help='Raster speed')
    raster.add_argument('-R',
                           metavar='Power',
                           gooey_options={
                                      'validator': {
                                          'test': '1 <= int(user_input) <= 100',
                                          'message': 'Must be between 1 and 100'
                                      }
                           },
                           help='Raster power')
    raster.add_argument('-s',
                           metavar='Size',
                           help='Photograph screen size (default 8)')

    vector.add_argument('-O',
                           metavar='Disable optimizations',
                           help='Disable vector optimization',
                           widget='BlockCheckbox')
    vector.add_argument('-f',
                           metavar='Frequency',
                           gooey_options={
                                      'validator': {
                                          'test': '1 <= int(user_input) <= 100',
                                          'message': 'Must be between 1 and 100'
                                      }
                           },
                           help='Vector frequency')
    vector.add_argument('-v',
                           metavar='Speed',
                           gooey_options={
                                      'validator': {
                                          'test': '1 <= int(user_input) <= 100',
                                          'message': 'Must be between 1 and 100'
                                      }
                           },
                           help='Vector speed')
    vector.add_argument('-V',
                           metavar='Power',
                           gooey_options={
                                      'validator': {
                                          'test': '1 <= int(user_input) <= 100',
                                          'message': 'Must be between 1 and 100'
                                      }
                           },
                           help='Vector power for the R, G, and B passes')
    vector.add_argument('-M',
                           metavar='Passes',
                           help='Number of times to repeat the R, G, and B passes')

    general.add_argument('filename', widget='FileChooser')

    parser.parse_args()

if __name__ == '__main__':
    main()
