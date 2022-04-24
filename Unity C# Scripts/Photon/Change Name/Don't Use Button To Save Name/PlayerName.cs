using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Photon.Pun;

public class PlayerName : MonoBehaviour
{
    //References
    public TMP_InputField nameTF;


    // Max and min names
    public void OnTFChangeMax()
    {
        if(nameTF.text.Length < 20) 
        {
            PhotonNetwork.NickName = nameTF.text;
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }else
        {
            
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }
    }

    public void OnTFChangeMin()
    {
        if(nameTF.text.Length > 0) 
        {
            PhotonNetwork.NickName = nameTF.text;
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }else
        {
            
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }
    }
    // Update
    void Update()
    {
        nameTF.text = PhotonNetwork.NickName.ToString();
    }
    // Save and load settings

    void SaveSettings()
     {
        PlayerPrefs.SetString("PlayerName", nameTF.text);
     }
     

     void LoadSettings()
     {
        if (PlayerPrefs.HasKey("PlayerName"))
            nameTF.text = 
                        PlayerPrefs.GetString("PlayerName");
        else
            nameTF.text = PhotonNetwork.NickName;
     }
}