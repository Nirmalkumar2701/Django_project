from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options: Any):

        titles = [
           "AI's Impact on Jobs",
           "Cybersecurity Trends 2025",
           "Future of Remote Work",
           "Blockchain Beyond Crypto",
           "Quantum Computing Breakthroughs",
           "Space Exploration Updates",
           "5G & 6G Revolution",
           "Tech for Climate Change",
           "US-China Tech War",
           "EVs vs Hydrogen Cars",
           "Metaverse: Future or Hype?",
           "Big Tech Regulations",
           "Biotech & Future Pandemics",
           "Global Economy Post-COVID",
           "Energy Crisis & Renewables",
           "Next-Gen Tech Startups",
           "Misinformation & Social Media",
           "Rise of Digital Nomads",
           "Smart Cities & AI",
           "Military AI Ethics"]

        contents = [
           "AI is transforming jobs by automating tasks, enhancing productivity, and creating new roles. However, concerns about job displacement and the need for reskilling remain critical.",
           "Cybersecurity in 2025 will focus on AI-driven threat detection, zero-trust security models, and stronger regulations to combat rising cyber threats, including ransomware and data breaches.",
           "Remote work is evolving into hybrid models, with AI and automation improving collaboration. Companies must balance flexibility with productivity and security challenges.",
           "Blockchain is expanding beyond cryptocurrency into supply chain management, secure voting systems, and decentralized finance (DeFi), offering transparency and security in various industries.",
           "Quantum computing is making strides, promising breakthroughs in encryption, drug discovery, and problem-solving, but challenges in stability and scalability remain.",
           "Space exploration is advancing with Mars missions, lunar bases, and commercial space travel. Companies like SpaceX and NASA are pushing the boundaries of human spaceflight.",
           "5G is revolutionizing connectivity, while 6G research is underway, promising ultra-fast speeds, lower latency, and seamless IoT integration to power smart cities and industries.",
           "Technology is playing a crucial role in climate change mitigation, with innovations in carbon capture, renewable energy, and AI-driven climate modeling helping reduce emissions.",
           "The US-China tech war is intensifying, with both nations competing in AI, semiconductor manufacturing, and cybersecurity, leading to trade restrictions and geopolitical tensions.",
           "EVs and hydrogen cars are competing as the future of transportation. While EVs dominate the market, hydrogen technology is gaining traction for long-range applications and sustainability.",
           "The Metaverse is developing as a virtual world for work, entertainment, and social interaction. While promising, concerns over privacy, accessibility, and real-world impact persist.",
           "Governments worldwide are introducing regulations to curb Big Tech monopolies, address data privacy concerns, and ensure ethical AI usage, affecting major corporations like Google and Meta.",
           "Biotech advancements are improving pandemic preparedness with mRNA vaccines, AI-driven drug discovery, and rapid testing, helping prevent future health crises.",
           "The global economy is recovering post-pandemic, facing inflation, supply chain disruptions, and changing labor markets, with emerging trends in digital and green economies.",
           "The energy crisis is accelerating the transition to renewables, with investments in solar, wind, and nuclear power aimed at reducing reliance on fossil fuels.",
           "Tech startups in AI, biotech, and fintech are emerging as industry leaders, with innovations in automation, health tech, and digital finance shaping the future.",
           "Misinformation on social media is a growing concern, with AI-driven fact-checking, stricter regulations, and digital literacy programs needed to combat fake news.",
           "Digital nomadism is on the rise, driven by remote work flexibility and co-working spaces. Countries are offering special visas to attract remote professionals.",
           "Smart cities are integrating AI, IoT, and automation for efficient urban management, but challenges like data privacy and infrastructure costs remain.",
           "AI in the military is advancing, raising ethical concerns over autonomous weapons, decision-making, and warfare risks, prompting calls for international regulations."]

        img_urls = [
            "https://fastly.picsum.photos/id/1/800/400",
            "https://fastly.picsum.photos/id/2/800/400",
            "https://fastly.picsum.photos/id/3/800/400",
            "https://fastly.picsum.photos/id/4/800/400",
            "https://fastly.picsum.photos/id/5/800/400",
            "https://fastly.picsum.photos/id/6/800/400",
            "https://fastly.picsum.photos/id/7/800/400",
            "https://fastly.picsum.photos/id/8/800/400",
            "https://fastly.picsum.photos/id/9/800/400",
            "https://fastly.picsum.photos/id/10/800/400",
            "https://fastly.picsum.photos/id/11/800/400",
            "https://fastly.picsum.photos/id/12/800/400",
            "https://fastly.picsum.photos/id/13/800/400",
            "https://fastly.picsum.photos/id/14/800/400",
            "https://fastly.picsum.photos/id/15/800/400",
            "https://fastly.picsum.photos/id/16/800/400",
            "https://fastly.picsum.photos/id/17/800/400",
            "https://fastly.picsum.photos/id/18/800/400",
            "https://fastly.picsum.photos/id/19/800/400",
            "https://fastly.picsum.photos/id/20/800/400"]

        for title, content, img_url in zip(titles, contents, img_urls):
             Post.objects.create(title=title, content=content, img_url=img_url)
             
        self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))