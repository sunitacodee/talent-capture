from app.models.province import Province
from app.models.district import District
from app.models.localbody import LocalBody
from app.models.localBodyWard import LocalBodyWard

class AddressSeeder:
    def __init__(self, db_session):
        self.session = db_session

    def run_all_address_seededs(self):
        """Executes the entire seeding pipeline sequentially."""
        print("🌱 Starting structural database seeding...")
        # self.seed_provinces()
        self.seed_districts()
        self.seed_local_bodies()
        self.seed_wards()
        print("🎉 Address data successfully Seeded!")

    def seed_provinces(self):
        provinces_data = [
            {"id": 1, "name_en": "Koshi Province", "name_np": "कोशी प्रदेश"},
            {"id": 2, "name_en": "Madhesh Province", "name_np": "मधेस प्रदेश"},
            {"id": 3, "name_en": "Bagmati Province", "name_np": "बागमती प्रदेश"},
            {"id": 4, "name_en": "Gandaki Province", "name_np": "गण्डकी प्रदेश"},
            {"id": 5, "name_en": "Lumbini Province", "name_np": "लुम्बिनी प्रदेश"},
            {"id": 6, "name_en": "Karnali Province", "name_np": "कर्णाली प्रदेश"},
            {"id": 7, "name_en": "Sudurpashchim Province", "name_np": "सुदूरपश्चिम प्रदेश"},
        ]
        
        for p in provinces_data:
            if not self.session.query(Province).get(p["id"]):
                self.session.add(Province(**p))
        self.session.commit()
        print("Provinces synced.")

    def seed_districts(self):
        koshi        = self.session.query(Province).filter_by(name_en="Koshi Province").first()
        Madhesh      = self.session.query(Province).filter_by(name_en="Madhesh Province").first()
        bagmati      = self.session.query(Province).filter_by(name_en="Bagmati Province").first()
        gandaki      = self.session.query(Province).filter_by(name_en="Gandaki Province").first()
        lumbini      = self.session.query(Province).filter_by(name_en="Lumbini Province").first()
        karnali      = self.session.query(Province).filter_by(name_en="Karnali Province").first()
        sudurpaschim = self.session.query(Province).filter_by(name_en="Sudurpashchim Province").first()

        districts_data = [
            # Koshi Province (1)
            {"province_id":koshi.id, "name_en": "Bhojpur", "name_np": "भोजपुर"},
            {"province_id":koshi.id, "name_en": "Dhankuta", "name_np": "धनकुटा"},
            {"province_id":koshi.id, "name_en": "Ilam", "name_np": "इलाम"},
            {"province_id":koshi.id, "name_en": "Jhapa", "name_np": "झापा"},
            {"province_id":koshi.id, "name_en": "Khotang", "name_np": "खोटाङ"},
            {"province_id":koshi.id, "name_en": "Morang", "name_np": "मोरङ"},
            {"province_id":koshi.id, "name_en": "Okhaldhunga", "name_np": "ओखलढुङ्गा"},
            {"province_id":koshi.id, "name_en": "Panchthar", "name_np": "पाँचथर"},
            {"province_id":koshi.id, "name_en": "Sankhuwasabha", "name_np": "सङ्खुवासभा"},
            {"province_id":koshi.id, "name_en": "Solukhumbu", "name_np": "सोलुखुम्बु"},
            {"province_id":koshi.id, "name_en": "Sunsari", "name_np": "सुनसरी"},
            {"province_id":koshi.id, "name_en": "Taplejung", "name_np": "ताप्लेजुङ"},
            {"province_id":koshi.id, "name_en": "Tehrathum", "name_np": "तेह्रथुम"},
            {"province_id":koshi.id, "name_en": "Udayapur", "name_np": "उदयपुर"},

            # Madhesh Province (2)
            {"province_id": Madhesh.id, "name_en": "Bara", "name_np": "बारा"},
            {"province_id": Madhesh.id, "name_en": "Dhanusha", "name_np": "धनुषा"},
            {"province_id": Madhesh.id, "name_en": "Mahottari", "name_np": "महोत्तरी"},
            {"province_id": Madhesh.id, "name_en": "Parsa", "name_np": "पर्सा"},
            {"province_id": Madhesh.id, "name_en": "Rautahat", "name_np": "रौतहट"},
            {"province_id": Madhesh.id, "name_en": "Saptari", "name_np": "सप्तरी"},
            {"province_id": Madhesh.id, "name_en": "Sarlahi", "name_np": "सर्लाही"},
            {"province_id": Madhesh.id, "name_en": "Siraha", "name_np": "सिराहा"},

            # Bagmati Province (3)
            {"province_id": bagmati.id, "name_en": "Bhaktapur", "name_np": "भक्तपुर"},
            {"province_id": bagmati.id, "name_en": "Chitwan", "name_np": "चितवन"},
            {"province_id": bagmati.id, "name_en": "Dhading", "name_np": "धादिङ"},
            {"province_id": bagmati.id, "name_en": "Dolakha", "name_np": "दोलखा"},
            {"province_id": bagmati.id, "name_en": "Kathmandu", "name_np": "काठमाडौं"},
            {"province_id": bagmati.id, "name_en": "Kavrepalanchok", "name_np": "काभ्रेपलाञ्चोक"},
            {"province_id": bagmati.id, "name_en": "Lalitpur", "name_np": "ललितपुर"},
            {"province_id": bagmati.id, "name_en": "Makwanpur", "name_np": "मकवानपुर"},
            {"province_id": bagmati.id, "name_en": "Nuwakot", "name_np": "नुवाकोट"},
            {"province_id": bagmati.id, "name_en": "Ramechhap", "name_np": "रामेछाप"},
            {"province_id": bagmati.id, "name_en": "Rasuwa", "name_np": "रसुवा"},
            {"province_id": bagmati.id, "name_en": "Sindhuli", "name_np": "सिन्धुली"},
            {"province_id": bagmati.id, "name_en": "Sindhupalchok", "name_np": "सिन्धुपाल्चोक"},

            # Gandaki Province (4)
            {"province_id": gandaki.id, "name_en": "Baglung", "name_np": "बागलुङ"},
            {"province_id": gandaki.id, "name_en": "Gorkha", "name_np": "गोरखा"},
            {"province_id": gandaki.id, "name_en": "Kaski", "name_np": "कास्की"},
            {"province_id": gandaki.id, "name_en": "Lamjung", "name_np": "लमजुङ"},
            {"province_id": gandaki.id, "name_en": "Manang", "name_np": "मनाङ"},
            {"province_id": gandaki.id, "name_en": "Mustang", "name_np": "मुस्ताङ"},
            {"province_id": gandaki.id, "name_en": "Myagdi", "name_np": "म्याग्दी"},
            {"province_id": gandaki.id, "name_en": "Nawalpur", "name_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"},
            {"province_id": gandaki.id, "name_en": "Parbat", "name_np": "पर्वत"},
            {"province_id": gandaki.id, "name_en": "Syangja", "name_np": "स्याङ्गजा"},
            {"province_id": gandaki.id, "name_en": "Tanahun", "name_np": "तनहुँ"},

            # Lumbini Province (5)
            {"province_id": lumbini.id, "name_en": "Arghakhanchi", "name_np": "अर्घाखाँची"},
            {"province_id": lumbini.id, "name_en": "Banke", "name_np": "बाँके"},
            {"province_id": lumbini.id, "name_en": "Bardiya", "name_np": "बर्दिया"},
            {"province_id": lumbini.id, "name_en": "Dang", "name_np": "दाङ"},
            {"province_id": lumbini.id, "name_en": "Eastern Rukum", "name_np": "पूर्वी रुकुम"},
            {"province_id": lumbini.id, "name_en": "Gulmi", "name_np": "गुल्मी"},
            {"province_id": lumbini.id, "name_en": "Kapilvastu", "name_np": "कपिलवस्तु"},
            {"province_id": lumbini.id, "name_en": "Nawalparasi West", "name_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"},
            {"province_id": lumbini.id, "name_en": "Palpa", "name_np": "पाल्पा"},
            {"province_id": lumbini.id, "name_en": "Pyuthan", "name_np": "प्युठान"},
            {"province_id": lumbini.id, "name_en": "Rolpa", "name_np": "रोल्पा"},
            {"province_id": lumbini.id, "name_en": "Rupandehi", "name_np": "रुपन्देही"},

            # Karnali Province (6)
            {"province_id": karnali.id, "name_en": "Dailekh", "name_np": "दैलेख"},
            {"province_id": karnali.id, "name_en": "Dolpa", "name_np": "डोल्पा"},
            {"province_id": karnali.id, "name_en": "Humla", "name_np": "हुम्ला"},
            {"province_id": karnali.id, "name_en": "Jajarkot", "name_np": "जाजरकोट"},
            {"province_id": karnali.id, "name_en": "Jumla", "name_np": "जुम्ला"},
            {"province_id": karnali.id, "name_en": "Kalikot", "name_np": "कालिकोट"},
            {"province_id": karnali.id, "name_en": "Mugu", "name_np": "मुगु"},
            {"province_id": karnali.id, "name_en": "Salyan", "name_np": "सल्यान"},
            {"province_id": karnali.id, "name_en": "Surkhet", "name_np": "सुर्खेत"},
            {"province_id": karnali.id, "name_en": "Western Rukum", "name_np": "पश्चिमी रुकुम"},

            # Sudurpashchim Province (7)
            {"province_id": sudurpaschim.id, "name_en": "Achham", "name_np": "अछाम"},
            {"province_id": sudurpaschim.id, "name_en": "Baitadi", "name_np": "बैतडी"},
            {"province_id": sudurpaschim.id, "name_en": "Bajhang", "name_np": "बझाङ"},
            {"province_id": sudurpaschim.id, "name_en": "Bajura", "name_np": "बाजुरा"},
            {"province_id": sudurpaschim.id, "name_en": "Dadeldhura", "name_np": "डडेलधुरा"},
            {"province_id": sudurpaschim.id, "name_en": "Darchula", "name_np": "दार्चुला"},
            {"province_id": sudurpaschim.id, "name_en": "Doti", "name_np": "डोटी"},
            {"province_id": sudurpaschim.id, "name_en": "Kailali", "name_np": "कैलाली"},
            {"province_id": sudurpaschim.id, "name_en": "Kanchanpur", "name_np": "कञ्चनपुर"},
        ]

        for d in districts_data:
            if not self.session.query(District).filter_by(province_id=d["province_id"], name_en=d["name_en"]).first():
                self.session.add(District(**d))
        self.session.commit()
        print("  ✅ Districts synced.")
        

        for d in districts_data:
            existing = self.session.query(District).filter_by(
                province_id=d["province_id"], 
                name_en=d["name_en"]
            ).first()
            if not existing:
                self.session.add(District(**d))
        self.session.commit()
        print("  ✅ Districts synced.")

    def seed_local_bodies(self):
        # Dynamically grab the lookup IDs generated by the database engine
        ktm_dist = self.session.query(District).filter_by(name_en="Kathmandu").first()
        lpt_dist = self.session.query(District).filter_by(name_en="Lalitpur").first()
        mrg_dist = self.session.query(District).filter_by(name_en="Morang").first()

        local_bodies_data = []
        
        if ktm_dist:
            local_bodies_data.extend([
                {"district_id": ktm_dist.id, "name_en": "Kathmandu Metropolitan City", "name_np": "काठमाडौं महानगरपालिका", "body_type": "Metropolitan"},
                {"district_id": ktm_dist.id, "name_en": "Budhanilkantha Municipality", "name_np": "बुढानीलकण्ठ नगरपालिका", "body_type": "Municipality"},
            ])
        if lpt_dist:
            local_bodies_data.extend([
                {"district_id": lpt_dist.id, "name_en": "Lalitpur Metropolitan City", "name_np": "ललितपुर महानगरपालिका", "body_type": "Metropolitan"},
            ])
        if mrg_dist:
            local_bodies_data.extend([
                {"district_id": mrg_dist.id, "name_en": "Biratnagar Metropolitan City", "name_np": "विराटनगर महानगरपालिका", "body_type": "Metropolitan"},
            ])

        for lb in local_bodies_data:
            existing = self.session.query(LocalBody).filter_by(
                district_id=lb["district_id"], 
                name_en=lb["name_en"]
            ).first()
            if not existing:
                self.session.add(LocalBody(**lb))
        self.session.commit()
        print("  ✅ Local Bodies synced.")

    def seed_wards(self):
        # Seed Wards for Kathmandu Metro (32 Wards)
        ktm_metro = self.session.query(LocalBody).filter_by(name_en="Kathmandu Metropolitan City").first()
        if ktm_metro:
            for ward in range(1, 33):
                existing = self.session.query(LocalBodyWard).filter_by(local_body_id=ktm_metro.id, ward_number=ward).first()
                if not existing:
                    self.session.add(LocalBodyWard(local_body_id=ktm_metro.id, ward_number=ward))

        # Seed Wards for Budhanilkantha (13 Wards)
        bkn_mun = self.session.query(LocalBody).filter_by(name_en="Budhanilkantha Municipality").first()
        if bkn_mun:
            for ward in range(1, 14):
                existing = self.session.query(LocalBodyWard).filter_by(local_body_id=bkn_mun.id, ward_number=ward).first()
                if not existing:
                    self.session.add(LocalBodyWard(local_body_id=bkn_mun.id, ward_number=ward))

        self.session.commit()
        print("  ✅ Wards configuration completed.")