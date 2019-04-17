#coding:utf-8
"""
基于隐马尔科夫模型的词性标注
"""

import codecs
from pyhanlp import *

outfile = open('../data/rmrb_pos.txt', 'wb')
with codecs.open('../data/rmrb.txt', 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        line = line.strip()
        if line:
            out_li = []
            for term in HanLP.segment(line):
                out_li.append('%s/%s' % (term.word, term.nature))
            out_str = u'%s\n' % (u' '.join(out_li))
            outfile.write(out_str.encode('utf-8', 'ignore'))
