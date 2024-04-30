# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn,options
from firebase_admin import initialize_app
from flask import Flask, request, jsonify
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

initialize_app()

@https_fn.on_request(
        cors=options.CorsOptions(
        cors_origins=[r"https://stylco-3dc2a.web.app"],
        cors_methods=["get", "post"],
    )
)
def on_request_example(req: https_fn.Request) -> https_fn.Response:
    data=req.get_json()
    text = data.get('text')
    hello=sia.polarity_scores(text)
    compound_score = str(hello['compound'])
    #result=analyze_sentiment(text)
    return ({"sentiment": compound_score})






import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./LandingScreenOption.module.css";

const LandingScreenOption = () => {
  const navigate = useNavigate();

  const onLandingScreenOption1ContainerClick = useCallback(() => {
    navigate("/landing-screen-option-2");
  }, [navigate]);

  const onSocialClick = useCallback(() => {
    navigate("/landing-screen-option-2");
  }, [navigate]);

  const onContinueContainerClick = useCallback(() => {
    navigate("/onboarding-step-2");
  }, [navigate]);

  return (
    <div
      className={styles.landingScreenOption1}
      onClick={onLandingScreenOption1ContainerClick}
    >
      <img className={styles.image11Icon} alt="" src="/image-11@2x.png" />
      <img
        className={styles.socialIcon}
        alt=""
        src="/social.svg"
        onClick={onSocialClick}
      />
      <div className={styles.continue} onClick={onContinueContainerClick}>
        <div className={styles.continueChild} />
        <b className={styles.alreadyHaveAn}>ALREADY HAVE AN ACCOUNT</b>
      </div>
      <div className={styles.landingScreenOption1Child} />
      <b className={styles.stylco}>StylCo</b>
    </div>
  );
};

export default LandingScreenOption;
