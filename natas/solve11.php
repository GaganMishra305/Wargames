<?php
function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}

// Default data (known plaintext)
$defaultdata = array("showpassword"=>"no", "bgcolor"=>"#ffffff");
$plaintext = json_encode($defaultdata);

// Your cookie value (paste it here)
$cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D"; // REPLACE WITH YOUR COOKIE

// Decode the cookie to get ciphertext
$ciphertext = base64_decode($cookie);

// XOR plaintext with ciphertext to get the key
$key = xor_encrypt($plaintext, $ciphertext);
echo "Key (repeating): " . $key . "\n";

// The key repeats, so find the pattern
echo "Likely key: " . substr($key, 0, 4) . "\n\n";

// Now create malicious cookie with showpassword=yes
$malicious = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
$malicious_json = json_encode($malicious);

// Use the key we found (typically "KNHL" or similar)
$actual_key = "KNHL"; // Adjust if different
$encrypted = xor_encrypt($malicious_json, $actual_key);
$malicious_cookie = base64_encode($encrypted);

echo "New cookie to set: " . $malicious_cookie . "\n";
?>