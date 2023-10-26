import argparse
import sys

class Cli:
    def __init__(self, markups: list, verbs: list):
        self.markups = markups
        self.verbs = verbs
    @staticmethod
    def run():
        return Cli(markups=["yml", "json"], verbs=["list", "migrate"]).execute()

    def execute(self):
        argparser = self._get_argparser()
        return argparser.parse_args(sys.argv[1:])

    def _get_argparser(self):
        argparser = argparse.ArgumentParser(sys.argv[0], description="mass repository deporter")
        argparser.add_argument("verb", type=str, help=("verb of action = [%s]" % " | ".join(self.verbs)))
        argparser.add_argument("-s", "--source", type=str, help=("generic source node, expect a path to a configuration file [%s]" % " | ".join(self.markups)))
        argparser.add_argument("-d", "--destination", type=str, help=("generic destination node, expect a path to a configuration file [%s]" % " | ".join(self.markups)))
        argparser.add_argument("-m", "--mirror", type=str, help=("generic mirror node, expect a path to a configuration file [%s]" % " | ".join(self.markups)))
        argparser.add_argument("-p", "--private", default=False, action="store_true", help="new repositories will be private")
        argparser.add_argument("-w", "--wiki", default=False, action="store_true", help="new repositories will have wiki enabled")
        argparser.add_argument("-u", "--update-db", default=False, action="store_true", help="force DB update")
        return argparser
