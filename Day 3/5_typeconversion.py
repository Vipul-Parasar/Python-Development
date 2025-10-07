

# Type Conversion in Python
#
# From \ To →        int()              float()            bool()              str()                 list()               tuple()              set()                dict()
# ---------------------------------------------------------------------------------------------------
# int                ✅ same            ✅ works           ✅ (0→F)           ✅ works              ❌                   ❌                   ❌                   ❌
# float              ✅ truncates       ✅ same            ✅ (0.0→F)         ✅ works              ❌                   ❌                   ❌                   ❌
# bool               ✅ (T→1,F→0)       ✅ (1.0/0.0)       ✅ same            ✅ works              ❌                   ❌                   ❌                   ❌
# str (numeric)      ✅ digits          ✅ numeric         ✅ (empty→F)       ✅ same               ✅list of chars      ✅tuple of chars     ✅set of chars       ❌
# list               ❌                 ❌                 ✅ (empty→F)       ✅ repr               ✅ same              ✅ works             ✅ works             ❌
# tuple              ❌                 ❌                 ✅ (empty→F)       ✅ repr               ✅ works             ✅ same              ✅ works             ❌
# set                ❌                 ❌                 ✅ (empty→F)       ✅ repr               ✅ works             ✅ works             ✅ same              ❌
# dict               ❌                 ❌                 ✅ (empty→F)       ✅ repr               ✅ keys              ✅ keys              ✅ keys              ✅ same
# ---------------------------------------------------------------------------------------------------

