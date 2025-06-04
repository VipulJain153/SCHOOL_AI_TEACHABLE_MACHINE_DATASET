from icrawler.builtin import GoogleImageCrawler

def download_images(keyword, folder_name, num_images=30):
    crawler = GoogleImageCrawler(storage={'root_dir': folder_name})
    crawler.crawl(keyword=keyword, max_num=num_images)

# Example usage:
download_images('Scottish Kilt traditional clothing', 'Kilt Test', 10)
download_images('Japanese Kimono traditional clothing', 'Kimono Test', 10)
download_images('West African Dashiki Kilt traditional clothing', 'Dashiki Test', 10)
#download_images('Japanese Kimono traditional clothing', 'Kimono', 2)
#download_images('West African Dashiki traditional clothing', 'Dashiki', 2)
