import glob

class SearchHandler:
    @staticmethod
    def search_for_file(args):
        if "name" in args:
            filename = args.name

            if filename is None:
                filename = "*"
        else:
            filename = "*"
        
        if "ext" in args:
            extension = args.ext

            if extension is None:
                extension = ".*"

            if extension[0] != ".":
                extension = "." + extension
        else:
            extension = ".*"

        if "path" in args:
            path = args.path

        if "deep" in args:
            deep = args.deep
        else:
            deep = False

        results = glob.glob(f"{path}/**/{filename}{extension}", recursive=deep)

        for result in results:
            print(result)

