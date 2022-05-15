using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using Photon.Pun;

public class PlayerName : MonoBehaviour
{
    public TMP_InputField nameTF;
    public Button setNameBtn;


    public void OnTFChangeMax()
    {
        if(nameTF.text.Length < 20) 
        {
            setNameBtn.interactable = true;
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }else
        {
            setNameBtn.interactable = false;
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }
    }
    

    public void OnTFChange()
    {
        if(nameTF.text.Length > 0) 
        {
            setNameBtn.interactable = true;
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }else
        {
            setNameBtn.interactable = false;
            PlayerPrefs.SetString("PlayerName", nameTF.text);
        }
    }

        

    public void OnClick_SetName()
    {
        PhotonNetwork.NickName = nameTF.text;
        PlayerPrefs.SetString("PlayerName", nameTF.text);
    }


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



    void Awake()
    {
        nameTF.text = PhotonNetwork.NickName.ToString();
    }

     public void Refresh_Name()
     {
         
     }
 
}
