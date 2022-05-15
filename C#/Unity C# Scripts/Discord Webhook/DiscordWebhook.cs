using System.Collections;
using System.Collections.Generic;
using UnityEngine.Networking;
using UnityEngine;
using TMPro;

public class DiscordWebhook : MonoBehaviour
{
    string webhook_link = "put your discord webhook link here";

    string feedbackMessage;

    public void SendFeedback()
    {
        feedbackMessage = "put your message here";
        StartCoroutine(SendWebhook(webhook_link, feedbackMessage, (success) =>
        {
            if (success)
                Debug.Log("Message Sent");
        }));
    }


    IEnumerator SendWebhook(string link, string message, System.Action<bool> action)
    {
        WWWForm form = new WWWForm();
        form.AddField("content", message);
        using (UnityWebRequest www = UnityWebRequest.Post(link, form))
        {
            yield return www.SendWebRequest();
        }
    }
}