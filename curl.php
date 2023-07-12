<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://www.machinools.com/api/classification/classify",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\n    \"text_input\": [\"Les différentes solutions pour faire garder ses enfants · La babysitter · L'assistante maternelle agréée · L'auxiliaire parentale ou nounou à domicile\"],\n    \"option\": \"Text\",\n    \"word_list\": [\"santé\", \"parent\", \"enfant\", \"politique\", \"mariage\", \"Immobilier\", \"cuisine\", \"vacances\"]\n}",
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
