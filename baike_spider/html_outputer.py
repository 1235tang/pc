# coding: utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','wb')
        fout.write("<html>".encode('utf-8'))
        fout.write("<body>".encode('utf-8'))
        fout.write("<table>".encode('utf-8'))

        for data in self.datas:
            fout.write("<tr>".encode('utf-8'))
            fout.write("<td>".encode('utf-8')+data['url'].encode('utf-8')+"</td>".encode('utf-8') )
            fout.write("<td>".encode('utf-8')+data['title'].encode('utf-8')+"</td>".encode('utf-8'))
            fout.write(data['summary'].encode('utf-8'))
            fout.write("</tr>".encode('utf-8'))

        fout.write("</table>".encode('utf-8'))
        fout.write("</body>".encode('utf-8'))
        fout.write("</html>".encode('utf-8'))

        fout.close()