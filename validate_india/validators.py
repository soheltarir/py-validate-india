from .base import Base
from .constants import PAN_REGEX, AADHAAR_REGEX, MOBILE_REGEX, GST_REGEX, ESIC_REGEX, IFSC_REGEX, UAN_REGEX


pan = Base(PAN_REGEX)
aadhaar = Base(AADHAAR_REGEX)
mobile = Base(MOBILE_REGEX)
gst = Base(GST_REGEX)
ifsc = Base(IFSC_REGEX)
esic = Base(ESIC_REGEX)
uan = Base(UAN_REGEX)
