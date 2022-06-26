import urllib.parse
import requests


def summarizer(content, maxlength, minlength):
    query_data = {
        "content": content,
        "maxlength": maxlength,
        "minlength": minlength
    }
    url = f"http://127.0.0.1:5000/summarizer?" + urllib.parse.urlencode(query_data)
    res = requests.get(url)
    print()
    print(res.text)


if __name__ == '__main__':
    context = """
            Citation and commencement
        1.  These Regulations may be cited as the Health Products (Medical Devices) Regulations 2010 and shall come into operation on 10th August 2010.
        Definitions
        2.  In these Regulations, unless the context otherwise requires —
        “active implantable medical device” means any active medical device that is intended by its product owner —
        (a)	to be introduced, either —
        (i)	by surgical or medical intervention, wholly or partially into the body of a human being; or
        (ii)	by medical intervention, into a body orifice; and
        (b)	to remain in place after the procedure;
        “active medical device” means any medical device —
        (a)	the operation of which depends on a source of electrical energy or any source of power other than that directly generated by a human body or gravity; and
        (b)	which acts by converting that energy,
        but does not include any medical device intended to transmit any energy, substance or other element between that medical device and a patient without any significant change to that energy, substance or element;
        “Authority’s website” means the Authority’s Internet website at http://www.hsa.gov.sg;
        [S 334/2016 wef 01/11/2016]
        “body orifice” means any natural opening in a human body, the external surface of any eyeball, or any permanent artificial opening, such as a stoma or permanent tracheotomy;
        “clinical purpose” means any of the specific purposes described in paragraph (a) of the definition of “Medical device” in the second column of item 1 of the First Schedule to the Act;
        [S 334/2016 wef 01/11/2016]
        [S 318/2018 wef 01/06/2018]
        “clinical research” has the same meaning as in regulation 2(1) of the Health Products (Therapeutic Products as Clinical Research Materials) Regulations 2016 (G.N. No. S 332/2016);
        [S 334/2016 wef 01/11/2016]
        “custom-made medical device” means a medical device that —
        (a)	is made at the request of a qualified practitioner and in accordance with the specifications of the qualified practitioner regarding the design characteristics or construction of the medical device;
        (b)	is intended to be used only in relation to a particular individual; and
        (c)	is not adapted from a mass-produced medical device;
        “field safety corrective action” means any action taken to reduce the risk of death or serious deterioration in the state of health of a person associated with the use of a medical device, including —
        """
    summarizer(context, maxlength=400, minlength=50)
