class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    # 搜集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 将数据输出到html页面中
    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'].encode('utf-8'))
            fout.write("<td>%s</td>"% data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"% data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()