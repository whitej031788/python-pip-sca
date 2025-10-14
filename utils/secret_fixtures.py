"""
DUMMY SECRETS FOR SCANNER TESTING ONLY
These are fake, non-functional secrets intended to trigger secret scanners.
Do NOT use in any real environment.
"""

# =========================
# AWS CREDENTIALS EXAMPLES
# =========================
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_SESSION_TOKEN = (
    "IQoJb3JpZ2luX2VjEOv//////////wEaCXVzLXdlc3QtMiJIMEYCIQCy9B0a1o8O1T3wVq5R8l0dQ6VZz"
    "B9q0xfgwq5U9w4WcQIhAPoV3Q0bRG3ZJXf1kzH7e6W+Wm8I3mF0+Zq1O8m7h6FOKuYCCNj//////////wEQ"
    "AxoMNDg3NTIwNTI2NTk4IkwQYk1hZ2ljVG9rZW4xMjM0NTY3ODkwMTIzNApHcnF5Wk9qT3hQd0ZkSEpZQmJD"
    "b2JpYWJjZGVmZ2hpamtsbW5vcHFy"
)

# =========================
# JWT TOKENS
# =========================
JWT_HS256 = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJzdWIiOiIxMjM0IiwibmFtZSI6IkRvZSBEZXYiLCJpYXQiOjE1MTYyMzkwMjJ9."
    "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
)

# =========================
# GITHUB TOKENS
# =========================
GITHUB_TOKEN = "ghp_0123456789abcdefghijklmnopqrstuvwxyzAB"
GITHUB_FINE_GRAINED = "github_pat_11AABBCCDD11EE22FF33GG44HH55II66JJ77KK88"

# =========================
# SLACK TOKENS
# =========================
SLACK_BOT_TOKEN = "xoxb-1234567890123-1234567890123-abcdefghijklmnopqrstuvwx"
SLACK_USER_TOKEN = "xoxp-1234567890123-1234567890123-abcdefghijklmnopqrstuvwx"

# =========================
# STRIPE
# =========================
STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"
STRIPE_PUBLISHABLE_KEY = "pk_live_51H8DP0abc123xyz456DEFghi789JKL0MNOpq"

# =========================
# GOOGLE
# =========================
GOOGLE_API_KEY = "AIzaSyA-abcdefghijklmnopqrstuvwxyzABCDE12345"

# =========================
# AZURE
# =========================
AZURE_STORAGE_CONNECTION_STRING = (
    "DefaultEndpointsProtocol=https;AccountName=examplestorage;"
    "AccountKey=AbCDefGhIJklMNopQRstuVWxYZ0123456789abcdEFGHijklMNOPqrSTUV==;"
    "EndpointSuffix=core.windows.net"
)

# =========================
# TWILIO
# =========================
TWILIO_ACCOUNT_SID = "AC0123456789abcdef0123456789abcdef"
TWILIO_AUTH_TOKEN = "0123456789abcdef0123456789abcdef"

# =========================
# MONGODB & POSTGRES URLS WITH CREDS
# =========================
MONGODB_URI = "mongodb://dbuser:dbpassword@mongo.example.com:27017/mydb?authSource=admin"
POSTGRES_URL = "postgres://pguser:pgpassword@localhost:5432/mydb"

# =========================
# NPM & GITLAB TOKENS
# =========================
NPM_TOKEN = "npm_0123456789abcdefghijklmnopqrstuvwxyzABCDE"
GITLAB_TOKEN = "glpat-0123456789abcdefABCDEF"

# =========================
# FACEBOOK APP SECRET (FAKE HEX)
# =========================
FACEBOOK_APP_SECRET = "0123456789abcdef0123456789abcdef"

# =========================
# PRIVATE KEYS (SHORTENED, FAKE)
# =========================
OPENSSH_PRIVATE_KEY = """
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEAw6h4b9Y8WmQe9YqN3bHn5FQm7KQv1wLm0o7eY4m7pQnJ5Yz5l5sd
2V1n1q6b8tXbkfS2e8gd7bZ+Z+9Yh+Y0o2i1uJ0LwY6Zk9Q2w==
-----END OPENSSH PRIVATE KEY-----
"""

RSA_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAuR2H1q3m7o3bX2Q2k1gG4hZz8rVyQv0JzJ8c2O2wJ3s5kH8Q
k3C8+Jg8q2d+PZ0S+2VnT6tHh+qQ4A1ZK0a1pQ7s0uA8P7kN7X3b5z0QdY7x1Xc3
EwIDAQABAoIBAQCfaKEyFakeKeyDataOnlyForTesting000000000000000000
-----END RSA PRIVATE KEY-----
"""

GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDgFakePrivateKeyOnly
ForScannerTestingDoNotUseInProd0000000000000000000000000000000000000000
-----END PRIVATE KEY-----
"""

# =========================
# BASIC AUTH IN URL
# =========================
BASIC_AUTH_URL = "https://admin:SuperSecretPassword123!@example.com/secure"

# =========================
# DOCKER CONFIG AUTH (FAKE BASE64)
# =========================
DOCKER_AUTH = "eyJhdXRocyI6eyJleGFtcGxlLmNvbSI6eyJhdXRoIjoiYWJjZGVmZ2hpamtsbW5vcHFyIn19fQ=="

# =========================
# RANDOM API TOKENS
# =========================
API_TOKEN = "token_abcdefghijklmnopqrstuvwxyz0123456789"
BEARER_TOKEN = "bearer_abcdefghijklmnopqrstuvwxyz0123456789"
