{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-10-8d8dd3f4e3ce>, line 29)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-10-8d8dd3f4e3ce>\"\u001b[1;36m, line \u001b[1;32m29\u001b[0m\n\u001b[1;33m    #self.log(f'Saved file')\u001b[0m\n\u001b[1;37m                            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "import scrapy\n",
    "\n",
    "class BookStoreSpider(scrapy.Spider):\n",
    "    name = \"S2-BookStore\"\n",
    "    \n",
    "    def start_requests(self):\n",
    "        #base_url = 'http://books.toscrape.com/catalogue/'\n",
    "        #i = 1\n",
    "        '''\n",
    "        for i in range(3):\n",
    "            \n",
    "            url = base_url + href_value\n",
    "        \n",
    "        '''\n",
    "        urls = [\n",
    "            'http://books.toscrape.com/',\n",
    "        ]\n",
    "          \n",
    "        for url in urls:\n",
    "            yield scrapy.Request(url=url, callback=self.parse)\n",
    "        \n",
    "    def parse(self, response):\n",
    "        \n",
    "        r = response.selector.xpath('//li[@class=\"next\"]/a/@href').get()\n",
    "        \n",
    "        with open(\"file.txt\",\"w\") as f:\n",
    "            f.write(r)\n",
    "            #f.write(type(r)\n",
    "        #self.log(f'Saved file')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
